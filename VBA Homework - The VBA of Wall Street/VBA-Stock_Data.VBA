Sub StockDataLoop():
For Each ws In Worksheets

    'Inserting Header Data Via cells
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Percent Change"
    ws.Cells(1, 12).Value = "Total Stock Volume"

    'Assigning all variables for calculations
        Dim i As Long
        Dim tickerValue As String
        Dim totalOpen As Double
        totalOpen = 0
        Dim totalVolume As Double
        totalVolume = 0
        Dim yearlyChange As Double
        yearlyChange = 0
        Dim percentChange As Long
        percentChange = 0
        Dim tickerRow As Long
        tickerRow = 2
        Dim lastRow As Long
        lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        Dim ClosePrice As Double
        ClosePrice = 0
        'create new variable for restart of yearly change ticker row( should be = i + 1)'
        totalOpen = ws.Cells(2, 3).Value


For i = 2 To lastRow
    

    
    'Conditionals for Ticker
    If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
        tickerValue = ws.Cells(i, 1).Value
        

        ClosePrice = ws.Cells(i, 6).Value
    
    'Conditionals for Yearly Change
        yearlyChange = ClosePrice - totalOpen

     If totalOpen <> 0 Then
    'Conditionals for Percent Change
        percentChange = (yearlyChange / totalOpen) * 100
      
    'Conditionals for Total Stock Volume
        totalVolume = totalVolume + ws.Cells(i, 7).Value
        
    
    'Print values'
        ws.Range("I" & tickerRow).Value = tickerValue
        ws.Range("K" & tickerRow).Value = (Str(percentChange) & "%")
        ws.Range("J" & tickerRow).Value = yearlyChange
        ws.Range("L" & tickerRow).Value = totalVolume

        'Reseting loop'
        totalVolume = 0
        tickerRow = tickerRow + 1
        ClosePrice = 0
        yearlyChange = 0
        totalOpen = ws.Cells(i + 1, 3).Value
    End If
    Else
        totalVolume = totalVolume + ws.Cells(i, 7).Value
    End If
        
Next i


    'Assigning colors to %
Dim yearlyChangeLastRow As Long

yearlyChangeLastRow = ws.Cells(Rows.Count, 10).End(xlUp).Row

For i = 2 To yearlyChangeLastRow
    
    If ws.Cells(i, 10).Value >= 0 Then
        ws.Cells(i, 10).Interior.ColorIndex = 4

    Else
        ws.Cells(i, 10).Interior.ColorIndex = 3

    End If

Next i
    
    'Instering Challenges portion %'
    ws.Cells(1, 16).Value = "Ticker"
    ws.Cells(1, 17).Value = "Value"
    ws.Cells(2, 15).Value = "Greatest % Increase"
    ws.Cells(3, 15).Value = "Greatest % Decrease"
    ws.Cells(4, 15).Value = "Greatest Total Volume"

    'Assigning variables'
    Dim PercentLastRow As Long
    PercentLastRow = ws.Cells(Rows.Count, 11).End(xlUp).Row
    Dim PercentIncrease As Double
    PercentIncrease = 0
    Dim PercentDecrease As Double
    PercentDecrease = 0

    'Challenge Loop'
    For i = 2 To PercentLastRow

    'Challenge Conditionals'
    If PercentIncrease < ws.Cells(i, 11).Value Then
        PercentIncrease = ws.Cells(i, 11).Value
        ws.Cells(2, 17).Value = PercentIncrease
        ws.Cells(2, 17).Style = "Percent"
        ws.Cells(2, 16).Value = ws.Cells(i, 9).Value
    ElseIf PercentDecrease > ws.Cells(i, 11).Value Then
        PercentDecrease = ws.Cells(i, 11).Value
        ws.Cells(3, 17).Value = PercentDecrease
        ws.Cells(3, 17).Style = "Percent"
        ws.Cells(3, 16).Value = ws.Cells(i, 9)
    End If

Next i

    'Instering Challenges portion greatest total Volume'
    Dim TotalLastRow As Long
    TotalLastRow = ws.Cells(Rows.Count, 11).End(xlUp).Row
    Dim GreatestTotalVol As Double
    GreatestTotalVol = 0

    'Loop'
    For i = 2 To TotalLastRow

    'Conditionals for total vol'
    If GreatestTotalVol < ws.Cells(i, 12).Value Then
        GreatestTotalVol = ws.Cells(i, 12).Value
        ws.Cells(4, 17).Value = GreatestTotalVol
        ws.Cells(4, 16).Value = ws.Cells(i, 9)
    End If

Next i

Next ws

End Sub


