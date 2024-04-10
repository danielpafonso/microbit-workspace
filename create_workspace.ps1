param (
    [Parameter(Mandatory=$true)][string]$foldername
 )

# check if desired folder already exists
if (Test-Path $foldername -PathType Container) {
    Write-Host("Workspace `"$foldername`" already exists")
    exit 0
}

# copy files
Write-Host("Creating Workspace `"$foldername`"")
Copy-Item -Path "stubs" -Destination $foldername -Recurse
Copy-Item "make.py" -Destination $foldername
