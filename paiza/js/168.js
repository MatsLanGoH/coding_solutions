process.stdin.resume();
process.stdin.setEncoding('utf8');
// 自分の得意な言語で
// Let's チャレンジ！！
process.stdin.on('data', function (chocoReceived) {
    var chocoReturned = chocoReceived > 0 ? chocoReceived * 3 : 1;

    console.log(chocoReturned);
});
