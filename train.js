/*
     MitTask #1

A-TASK: 

Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

function mitTask(mit, task) {
  return task.split(mit).length - 1;
}

console.log(mitTask("e", "engineer"));
