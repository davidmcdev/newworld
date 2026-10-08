| Pregunta | Campo o valor elegido | Justificación |
| --- | --- | --- |
| ¿Qué evento demuestra que la cacería terminó? | hunt_completed | La fila de este evento nos muestra que el personaje estuvo ese día cazando |
| ¿Quién la completó? | villager_id | La columna muestra el aldeano encargado de la cacería pr lo tanto quien la colectó. |
| ¿Qué presa aparece registrada? | prey_type | Esta columna muestra los diferentes presas que se han cazado en la cacería. |
| ¿Cuándo ocurrió? | tick | Esta columna nos indica el tick exacto en el que ocurrió. |
| ¿A qué partida pertenece? | run_id | Esta otra columna nos muestra la ejecución con la que tuvo suceso el evento. |
| ¿Cómo localizo el evento original sin confundirlo con otro? | run_id y event_index | Estas dos columnas nos permiten identificar de forma sencilla el evento. |

Explica también por qué `activity`, `food_stock` y `amount_delta` no son necesarios para este parte. ¿Permite el evento saber por sí solo cuánta comida produjo la cacería?

Esos tres campos no son necesarios en este evento ya que son de utilidad en el evento cuando el personaje almacena la comida. No, es necesario ver posteriormente el evento con el cambio de la cantidad del recurso.


### Responde justificando cada decisión:

1. «Hay seis filas, por tanto hay seis cazadores distintos». ¿Es necesariamente cierto?

No, ya que un mismo personaje puede haber cazado varias veces y otros ninguna.

2. «Una fila indica que ese aldeano estuvo cazando durante todo el día». ¿Qué registra realmente la fila?

Registra el run_id, event_index, villager_id, prey_type y el día generado con los ticks.

3. «Borro del DataFrame original todas las filas con algún `NaN` y después selecciono las cacerías». ¿Por qué puede desaparecer información válida?

Puede desapecer información valiosa ya que pueden haber filas que contengas datos sobre las cacerías como en este caso y que alguna de sus columnas por alguna razón no se ha escrito perdiendo toda la información de la fila haciendo que los datos varíen.

4. «El CSV está vacío, así que nadie intentó cazar». ¿Qué puedes afirmar realmente sobre el registro?

Demuestra que la función de filtrado funciona correctamente ya que si no ha habido registros es porque esa fila no existe.