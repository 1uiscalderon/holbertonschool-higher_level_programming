#!/usr/bin/node
let datos = 0;
if (process.argv.length <= 3) {
  console.log(datos);
} else {
  datos = process.argv.slice(2);
  datos.sort().reverse();
  console.log(datos[1]);
}
