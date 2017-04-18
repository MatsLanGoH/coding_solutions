process.stdin.resume();
process.stdin.setEncoding('utf8');
// 自分の得意な言語で
// Let's チャレンジ！！
process.stdin.on('data', function (str) {
    var reg = /False/gi;  // replace all instances of "False"
    var output = str.replace(reg, "True");  // FalseをTrueに置き換える
    console.log(output);
});
