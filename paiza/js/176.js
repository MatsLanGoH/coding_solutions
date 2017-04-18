process.stdin.resume();
process.stdin.setEncoding('utf8');
// 自分の得意な言語で
// Let's チャレンジ！！
process.stdin.on('data', function (chunk) {
    var number = chunk.toString()[0];  // 百の位をスライスする
    var output;

    // 出力ロジック
    if (number == 2) {
        output = "ok";
    } else if (number == 4) {
        output = "error";
    } else {
        output = "unknown";
    }
    console.log(output);
});
