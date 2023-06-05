DetalleVenta.objects.values('detVenta__venFecha').annotate(totalVentasPorDia = Sum('detValorDetalle'))
[{'detVenta__venFecha': datetime.date(2023, 4, 2), 'totalVentasPorDia': 6300000}, 
{'detVenta__venFecha': datetime.date(2023, 4, 16), 'totalVentasPorDia': 5037000}, 
{'detVenta__venFecha': datetime.date(2023, 4, 30), 'totalVentasPorDia': 9000000}, 
{'detVenta__venFecha': datetime.date(2023, 5, 7), 'totalVentasPorDia': 4498000}, 
{'detVenta__venFecha': datetime.date(2023, 5, 14), 'totalVentasPorDia': 809000}, 
{'detVenta__venFecha': datetime.date(2023, 5, 21), 'totalVentasPorDia': 999000}, 
{'detVenta__venFecha': datetime.date(2023, 5, 28), 'totalVentasPorDia': 13500000}, 
{'detVenta__venFecha': datetime.date(2023, 6, 1), 'totalVentasPorDia': 6669000}]


DetalleVenta.objects.values('detVenta__venFecha__month').annotate(totalVentasPorMes = Sum('detValorDetalle'))
[{'detVenta__venFecha__month': 4, 'totalVentasPorMes': 20337000}, 
{'detVenta__venFecha__month': 5, 'totalVentasPorMes': 19806000}, 
{'detVenta__venFecha__month': 6, 'totalVentasPorMes': 6669000}]
