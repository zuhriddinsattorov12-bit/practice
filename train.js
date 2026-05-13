/*
MITASK L

Shunday function yozing, u string qabul qilsin va string ichidagi hamma sozlarni chappasiga yozib va sozlar ketma-ketligini buzmasdan stringni qaytarsin.
MASALAN: reverseSentence("we like coding!") return "ew ekil gnidoc";
*/

function reverseSentence(sentence) {
  return sentence
    .split(" ")
    .map((word) => word.split("").reverse().join(""))
    .join(" ");
}

console.log(reverseSentence("Study in MIT!"));

/*
Mitask J

J-TASK (NodeJS)

Shunday function yozing, u parametridagi array ichida eng kop takrorlangan raqamni topib qaytarsin.
MASALAN: majorityElement([1,2,3,4,5,4,3,4]) return 4
*/

// const numbers = [1, 2, 3, 1, 3, 1, 6, 1, 2];

// function getrepeatedMost(arr) {
//   const sorted = arr.sort((a, b) => a - b);

//   let maxCount = 0;
//   let repeatedMost = sorted[0];
//   let currentCount = 1;

//   for (let i = 1; i < sorted.length; i++) {
//     if (sorted[i] === sorted[i - 1]) {
//       currentCount++;
//     } else {
//       currentCount = 1;
//     }

//     if (currentCount > maxCount) {
//       maxCount = currentCount;
//       repeatedMost = sorted[i];
//     }
//   }

//   return repeatedMost;
// }

/*
Mitask I

Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
MASALAN: get_digits("m14i1t") return qiladi "141"
*/

// def get_digits(text):
//     return "".join(char for char in text if char.isdigit())

// print(get_digits("asd123"))

/* 
H-TASK (NodeJS)

shunday function tuzing, u integerlardan iborat arrayni argument sifatida qabul qilib, faqat positive qiymatlarni olib string holatda return qilsin
MASALAN: getPositive([1, -4, 2]) return qiladi "12"
*/

// function numbers(mit) {
//   return mit.filter((m) => m > 0).join("");
// }

// console.log("result:", numbers([3, -3, 7]));

// const numbers = [3, -3, 7];
// const result = numbers.filter((mit) => mit > 0).join(" ");

// console.log("result", result);

/* 
G-TASK (PYTHON)

Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
*/

/* Mitask #6 (F)
F-TASK (NodeJS)

Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
MASALAN: getReverse("hello") return true return qiladi

*/

// function mitLetters(str) {
//   return new Set(str).size < str.length;
// }

// console.log(mitLetters("hello")); // true
// console.log(mitLetters("world")); // false

/* MitTask # 5 (E)
E-TASK (NodeJS)

Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"
*/

// function getReverse(a) {
//   return a.split("").reverse().join("");
// }

// const Steve = "MIT";
// const zzz = getReverse(Steve);

// console.log(zzz);

/* MitTask # 4

Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
*/

// const numbers = [3, 21, 5, 6, 7];

// function getHighestIndex(arr) {
//   const max = Math.max(arr);
//   return arr.indexOf(max);
// }

// console.log("index:", getHighestIndex(numbers));

/* MitTask #3
C-TASK (NodeJS)

Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
 */

// function mitTask(str1, str2) {
//   if (str1.length !== str2.length) return false;

//   const counter = {};

//   for (let mit of str1) {
//     counter[mit] = (counter[mit] || 0) + 1;
//   }

//   for (let mit of str2) {
//     if (!counter[mit]) return false;
//     counter[mit]--;
//   }

//   return true;
// }

// console.log(mitTask("mitgroup", "gmitprou")); // true

/* MitTask #2 

B-TASK (Nodejs) Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
*/

// function mitTask(str) {
//   let count = 0;
//   for (let i = 0; i < str.length; i++) {
//     if (str[i] >= "0" && str[i] <= "9") {
//       count++;
//     }
//   }
//   return count;
// }

// console.log(mitTask("Year 2005")); // 4

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

// mit reverse(a):
//     b = ""
//     for i of reverse:
//     b = i + b

//     print(b)

// reverse("lsdkjfskf")
