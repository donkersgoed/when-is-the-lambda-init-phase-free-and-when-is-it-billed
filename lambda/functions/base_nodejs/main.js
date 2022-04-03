const INIT_SLEEP = parseInt(process.env.INIT_SLEEP);
const HANDLER_SLEEP = parseInt(process.env.HANDLER_SLEEP);

console.log("Handler starting");
console.log("Sleep for " + INIT_SLEEP + " second(s)");
var waitTill = new Date(new Date().getTime() + INIT_SLEEP * 1000);
while (waitTill > new Date()) {}
console.log("Handler done");

exports.handler = async function (_event, _context) {
  console.log("Handler starting");
  console.log("Sleep for " + HANDLER_SLEEP + " second(s)");
  var waitTill = new Date(new Date().getTime() + HANDLER_SLEEP * 1000);
  while (waitTill > new Date()) {}
  console.log("Handler done");
};
