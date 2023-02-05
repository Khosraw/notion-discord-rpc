$windowTitles = @()
$visibleProcesses = @()
$visibleProcessesWithWindows = @()

Get-Process | Where-Object {$_.MainWindowTitle -ne ""} | ForEach-Object {
    $processName = $_.ProcessName

    if ($processName -like "Notion*") {
        Write-Output $_.MainWindowTitle
	    break
    }
}