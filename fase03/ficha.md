| Pregunta | Tabla y columnas necesarias | Operación y motivo |
| --- | --- | --- |
| ¿Cuántas cacerías completadas se registraron? | run_id,event_index,tick,villager_id,prey_type,simulation_day | Suma de todas las filas que se hay en el documento |
| ¿Cuántas corresponden a cada tipo de presa? | prey_type | Contar los valores por tipo de presa |
| ¿Qué porcentaje representa cada presa? | prey_type | Una vez que se tienen agrupadas las presas se hace el cálculo sobre 100 |
| ¿Cuántas cacerías se registraron en cada día observado? | simulation_day | Contar las cacerías agrupándolas por días |
| ¿Cuánto aumentó, disminuyó y cambió en términos netos la comida? | amount_before,amount_after,amount_delta | Sobre el delta y los incrementos y decrementos se pueden realizar las operaciones matemáticas necesarias |

Responde utilizando tus resultados reales:

1. ¿Qué presa o presas tienen el mayor recuento? Si hay empate, indícalo; si no hay datos, explica por qué no puedes responder.

La oveja es la presa más veces cazada.

2. ¿El porcentaje de una presa representa porcentaje de cacerías, de aldeanos o de tiempo? Justifica el denominador.

Sí ya que te puedes hacer una idea de las veces que se ha ido a cazar el personaje ya que no se va a llevar todas las presas en una sola cacería justificando además el tiempo dedicado por dicho aldeano en las cacerías.

3. ¿El día con más cacerías fue necesariamente el día en que se dedicó más tiempo a cazar?

No tiene por qué. Hay días que pueden haber una mayor cantidad de presas o que la cacería fuera mayor y otros aunque sea menor puede ser que haya tenido menos suerte en dichas cateforías.

4. ¿El balance neto indica las existencias finales de comida? ¿Qué información faltaría?

No del todo, ya que es posible que parte de las existencias sean consumidas por los aldeanos y esto no es recogido en las cacerías.

5. ¿Puedes demostrar que todos los incrementos de comida se deben a la caza? ¿Qué vínculo entre eventos necesitarías para justificarlo?

Sí, todos los incrementos de comida se debe a ello. Pues habría que relacionar las cacerías con el incremento de recursos para poder obtenerlo.