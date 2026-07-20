"""Small 2D cross-correlation and detection geometry, without image dependencies."""
import math


def rectangle(matrix):
    return bool(matrix and matrix[0] and all(len(row)==len(matrix[0]) for row in matrix))


def conv2d_valid(image,kernel,stride=1):
    # Deep-learning convolution is normally cross-correlation: no kernel flip.
    if not rectangle(image) or not rectangle(kernel) or type(stride) is not int or stride<=0:
        raise ValueError("invalid matrix/stride")
    h,w,kh,kw=len(image),len(image[0]),len(kernel),len(kernel[0])
    if kh>h or kw>w: raise ValueError("kernel exceeds image")
    return [[sum(image[y+i][x+j]*kernel[i][j] for i in range(kh) for j in range(kw))
             for x in range(0,w-kw+1,stride)] for y in range(0,h-kh+1,stride)]


def box_area(box):
    if len(box)!=4 or any(not math.isfinite(x) for x in box) or box[2]<box[0] or box[3]<box[1]:
        raise ValueError("box must be finite ordered xyxy")
    return (box[2]-box[0])*(box[3]-box[1])


def iou(a,b):
    aa,bb=box_area(a),box_area(b)
    intersection=max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))
    union=aa+bb-intersection
    return intersection/union if union else 0.0


def nms(boxes,scores,threshold=0.5):
    if len(boxes)!=len(scores) or not 0<=threshold<=1 or any(not math.isfinite(s) for s in scores):
        raise ValueError("invalid NMS input")
    for box in boxes: box_area(box)
    pending=sorted(range(len(boxes)),key=lambda i:(-scores[i],i))
    kept=[]
    while pending:
        i=pending.pop(0)
        kept.append(i)
        pending=[j for j in pending if iou(boxes[i],boxes[j])<=threshold]
    return kept


def main():
    import json
    boxes=[[0,0,2,2],[0,0,2,2],[3,3,4,4]]
    print(json.dumps({"convolution":conv2d_valid([[1,2,3],[4,5,6],[7,8,9]],[[1,0],[0,-1]]),
                      "partial_iou":iou([0,0,2,2],[1,1,3,3]),
                      "nms_indices":nms(boxes,[0.9,0.8,0.7])},indent=2))


if __name__=="__main__": main()
