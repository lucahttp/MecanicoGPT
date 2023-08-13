
sudo apt install tesseract-ocr

apt install ocrmypdf
# apt-cache search tesseract-ocr
tesseract-ocr-spa tesseract-ocr-eng



ocrmypdf -l eng --force-ocr /mnt/c/data/Mortimer/OCR/perkins-workshop-manual-for-diesel-engines-d4-203-4-203-4-192-1979.pdf output.pdf
ocrmypdf -l esp --force-ocr /mnt/c/data/Mortimer/OCR/perkins-workshop-manual-for-diesel-engines-d4-203-4-203-4-192-1979.pdf output.pdf


python -m ocrmypdf 

--user

choco install tesseract
choco install ghostscript

$folderPath = ".\originalFiles\"
$pythonCommand = "python -m ocrmypdf -l spa --force-ocr"
$outputFolder = ".\originalFiles\processed\"

Get-ChildItem -Path "$folderPath" -File | ForEach-Object {
    $filename = $_.BaseName -replace "\\+\\", ""
    #echo $_
    #echo $filename

    # $outputFilePath = Join-Path $outputFolder -ChildPath $filename + ".pdf"
    $outputFilePath = $outputFolder + $filename + ".pdf"
    echo $outputFilePath
    #$outputFilePath = $outputFilePath -replace "+", ""
    $command = "$pythonCommand `"$($_.FullName)`" `"$outputFilePath`""
    Invoke-Expression $command
}


https://ocrmypdf.readthedocs.io/en/latest/languages.html
C:\\Program Files\\Tesseract-OCR\\tessdata
C:\Program Files\Tesseract-OCR\tessdata