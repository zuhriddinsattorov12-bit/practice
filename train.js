/*
     MitTask #1

A-TASK: 

Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

// function mitTask(mit, task) {
//   return task.split(mit).length - 1;
// }

// console.log(mitTask("e", "engineer"));

/* MitTask #2 

B-TASK (Nodejs) Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
*/

function mitTask(str) {
  let count = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] >= "0" && str[i] <= "9") {
      count++;
    }
  }
  return count;
}

console.log(mitTask("Year 2005")); // 4
