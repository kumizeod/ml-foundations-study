param(
    [ValidateSet('2026-07','2026-08','2026-09')]
    [string]$Through = '2026-09',
    [ValidatePattern('^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$')]
    [string]$Repository = 'kumizeod/ml-foundations-study'
)
$ErrorActionPreference = 'Stop'
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw 'Git for Windows is required. Install it and reopen PowerShell.'
}
$statePath = Join-Path $PSScriptRoot '.git/study-checkpoints.json'
if (-not (Test-Path $statePath)) { throw 'Missing .git/study-checkpoints.json. Extract the complete ZIP including .git.' }
$state = Get-Content -Raw $statePath | ConvertFrom-Json
$commit = $state.checkpoints.PSObject.Properties[$Through].Value
if (-not $commit -or $commit -notmatch '^[0-9a-f]{40}$') { throw 'Invalid checkpoint.' }
& git -C $PSScriptRoot cat-file -e "${commit}^{commit}"
if ($LASTEXITCODE -ne 0) { throw 'Commit is missing from the extracted repository.' }
$dirty = & git -C $PSScriptRoot status --porcelain
if ($LASTEXITCODE -ne 0) { throw 'Cannot inspect working tree.' }
if ($dirty) { throw 'Working tree has changes. Inspect or save them before publishing.' }
$remoteUrl = "https://github.com/$Repository.git"
Write-Host "Pushing $Through checkpoint $commit to $remoteUrl"
& git -C $PSScriptRoot push $remoteUrl "${commit}:refs/heads/main"
if ($LASTEXITCODE -ne 0) { throw 'Push failed. Check repository creation and Windows Git authentication; do not regenerate history.' }
$remote = & git -C $PSScriptRoot ls-remote --heads $remoteUrl main
if ($LASTEXITCODE -ne 0 -or -not ($remote -match "^$commit\s")) { throw 'Could not verify the expected remote main.' }
Write-Host 'Remote main verified. Later checkpoints were not pushed.'
