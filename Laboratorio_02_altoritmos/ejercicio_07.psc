Algoritmo ejercicio_07
	Definir ST, IGV, Q, QT, SN Como Real;
	Escribir 'Usted recibe el sueldo de 930' ;
	Escribir 'ST = 930';
	Escribir 'Debera restar un I.G.V. equivalente a un 11%';
	ST <- 930;
	IGV <- (ST-ST*0.11);
	Escribir 'Su sueldo actual con descuento de I.G.V. es: ', IGV;
	Escribir 'Ahora deberá sumar el adelanto de quincena';
	Q <- (ST/2);
	QT <- (Q*0.30);
	SN <- (IGV+QT);
	Escribir 'su sueldo neto es equivalente a: S/.',SN;
FinAlgoritmo
