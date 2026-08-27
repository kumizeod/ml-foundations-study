"""Sequence-level teaching operators with explicit masking contracts."""
from .nlp import attention, cross_entropy


def causal_attention(queries, keys, values):
    """Self-attention over equal-length sequences; position t reads <=t."""
    if not queries or len(queries) != len(keys) or len(keys) != len(values):
        raise ValueError('causal self-attention needs equal nonempty lengths')
    outputs, weights = [], []
    for t, query in enumerate(queries):
        output, row = attention(query, keys, values,
                                allowed=[j <= t for j in range(len(keys))])
        outputs.append(output)
        weights.append(row)
    return outputs, weights


def masked_cross_entropy(logits, targets, valid):
    """Mean over valid tokens, not over padded sequence length."""
    if not logits or len(logits) != len(targets) or len(targets) != len(valid):
        raise ValueError('logits, targets and valid must have equal nonempty length')
    if any(type(x) is not bool for x in valid):
        raise ValueError('valid must contain booleans')
    losses = [cross_entropy(z, y) for z, y, keep in zip(logits, targets, valid) if keep]
    if not losses:
        raise ValueError('no valid target: average loss is undefined')
    return sum(losses) / len(losses)
