# Investigación sobre RAID

## 1. ¿Qué es RAID?

RAID (Redundant Array of Independent Disks) es una tecnología que combina varios discos duros para mejorar el rendimiento y la seguridad de los datos. Dependiendo de cómo se configuren los discos, se pueden obtener diferentes beneficios.

## 2. Historia de RAID

RAID fue propuesto por primera vez en 1987 por los investigadores **David A. Patterson**, **Garth A. Gibson** y **Randy H. Katz** en la Universidad de California, Berkeley. Su objetivo era mejorar el rendimiento y la fiabilidad de los sistemas de almacenamiento utilizando discos duros más baratos y pequeños.



## 3. Tipos de RAID

Existen varios niveles de RAID, cada uno con características específicas:

- **RAID 0 (Striping):** Divide los datos entre dos o más discos para mejorar la velocidad. No ofrece redundancia; si un disco falla, se pierden todos los datos.

- **RAID 1 (Mirroring):** Duplica los datos en dos discos. Si un disco falla, los datos siguen disponibles en el otro.

- **RAID 5 (Striping con paridad):** Distribuye los datos y la paridad entre tres o más discos. Permite la recuperación de datos si un disco falla.

- **RAID 6 (Doble paridad):** Similar al RAID 5, pero con dos bloques de paridad. Puede soportar la falla de dos discos simultáneamente.

- **RAID 10 (1+0):** Combina RAID 1 y RAID 0. Ofrece alta velocidad y redundancia, pero requiere al menos cuatro discos.

## 4. Ventajas de RAID

- **Mejora del rendimiento:** Algunos niveles de RAID, como el RAID 0, aumentan la velocidad de lectura y escritura.

- **Redundancia de datos:** Niveles como RAID 1 y RAID 5 proporcionan copias de seguridad automáticas de los datos.

- **Escalabilidad:** Es posible agregar más discos para aumentar la capacidad de almacenamiento.

## 5. Desventajas de RAID

- **Costo:** Algunos niveles de RAID requieren más discos, lo que incrementa el costo.

- **Complejidad:** La configuración y mantenimiento de RAID pueden ser complicados.

- **No reemplaza los respaldos:** Aunque RAID ofrece redundancia, no sustituye la necesidad de realizar copias de seguridad regulares.

## 6. Conclusión

RAID es una herramienta útil para mejorar el rendimiento y la seguridad de los datos. La elección del nivel de RAID adecuado depende de las necesidades específicas de cada usuario o empresa.

## 7. Referencias

- FS.COM. (2019). *¿Qué es RAID? Tipos, ventajas y cuál elegir para tu empresa*. Recuperado de https://www.fs.com/es/blog/what-is-raid-types-advantages-and-which-one-to-choose-for-your-company-5317.html

- Pronetic. (2022). *Almacenamiento RAID: Tipos y Cuál Elegir*. Recuperado de https://pronetic.geeknetic.es/Guia/3027/Almacenamiento-RAID-Tipos-y-Cual-Elegir.html


