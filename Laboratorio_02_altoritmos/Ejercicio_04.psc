Algoritmo Ejercicio_04
	Definir H,B, R, Ac, Vc  Como Real;
	Escribir 'Ingrese la altura del c�lindro';
	Leer H;
	Escribir 'Ingrese la base del cilindro';
	Leer B;
	R <- (B/2);
	Escribir 'El radio del cilindro es: ', R;
	Ac <- ((2*PI)*(R)*(H)+(2*PI)*(R*R));
	Escribir 'El �rea del cilindro es: ', Ac;
	Escribir 'Ahora conociendo que el �rea es: ',Ac;
	Vc <- (PI*(R*R))*H;
	Escribir 'El volumen del cilindro es: ', Vc;
FinAlgoritmo
