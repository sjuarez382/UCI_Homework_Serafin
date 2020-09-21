Sub StockDataLoop():
For Each ws in Worksheets

	'Inserting Header Data Via cells
	ws.Cells(1, 9).Value = "Ticker"
	ws.Cells(1, 10).Value = "Yearly Change"
	ws.Cells(1, 11).Value = "Percent Change"
	ws.Cells(1, 12).Value = "Total Stock Volume"

	'Assigning all variables for calculations
		Dim i As Long
		Dim tickerValue As String
		Dim totalOpen As Double
		Dim totalVolume As Double
		totalVolume = 0
		Dim yearlyChange As Double
		yearlyChange = 0
		Dim percentChange As Double
		Dim tickerRow As Long
		tickerRow = 2
		Dim lastRow As Long
		lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
		

for i = 2 to lastRow
		totalOpen = ws.cells(tickerRow, 3).Value
	
	'Conditionals for Ticker
	if ws.cells(i + 1, 1).Value <> ws.cells(i , 1).Value then 
		tickerValue = ws.cells(i , 1).Value
		ws.range("I" & tickerRow).Value = tickerValue
	
	'Conditionals for Yearly Change
		yearlyChange = close - totalOpen
		ws.range("J" & tickerRow).Value = yearlyChange


	'Conditionals for Percent Change
		percentChange = ( yearlyChange/ totalOpen)
		ws.range("K" & tickerRow).Value = percentChange
		ws.range("K" & tickerRow).style = "Percent"

	'Conditionals for Total Stock Volume 
		totalVolume = totalVolume + ws.cells(i, 7).Value
		ws.range("L" & tickerRow).Value = totalVolume

		tickerRow = tickerRow + 1
		totalOpen = ws.cells(tickerRow, 3).Value
		yearlyChange = 0
		totalVolume = 0
	else
		totalVolume = totalVolume + ws.cells(i, 7).Value
	End If 
		
Next i 


	'Assigning colors to %
Dim yearlyChangeLastRow As Long 

yearlyChangeLastRow = ws.Cells(Rows.Count, 10).End(xlUp).Row 

for i = 2 to yearlyChangeLastRow
	
	if ws.cells(i , 10).Value >= 0 Then 
		ws.cells(i , 10).interior.ColorIndex = 4

	else 
		ws.cells(i , 10).interior.ColorIndex = 3

	End if 

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
	Dim	PercentIncrease As Double
	PercentIncrease = 0
	Dim PercentDecrease As Double
	PercentDecrease = 0

	'Challenge Loop'
	For i = 2 to PercentLastRow

	'Challenge Conditionals'
	if PercentIncrease < ws.Cells(i, 11).Value Then
		PercentIncrease = ws.Cells(i, 11).Value
		ws.Cells(2, 17).Value = PercentIncrease
		ws.Cells(2, 17).Style = "Percent"
		ws.Cells(2, 16).Value = ws.Cells(i, 9).Value
	elseIf	PercentDecrease > ws.Cells(i, 11).Value Then
		PercentDecrease = ws.Cells(i, 11).Value
		ws.Cells(3, 17).Value = PercentDecrease
		ws.Cells(3, 17).Style = "Percent"
		ws.Cells(3, 16).Value = ws.Cells(i, 9)
	End if 

Next i 

	'Instering Challenges portion greatest total Volume'
	Dim TotalLastRow As Long
	TotalLastRow = ws.Cells(Rows.Count, 11).End(xlUp).Row
	Dim GreatestTotalVol as Double
	GreatestTotalVol = 0

	'Loop'
	For i = 2 to TotalLastRow

	'Conditionals for total vol'
	If GreatestTotalVol < ws.Cells(i, 12).Value Then
		GreatestTotalVol = ws.Cells(i, 12).Value 
		ws.Cells(4, 17).Value = GreatestTotalVol
		ws.Cells(4, 16).Value = ws.Cells(i, 9)
	End If

Next i

Next ws 

End Sub
