use std::{cmp::Ordering, io};
// Rng是一个trait（特征），定义了随机数生成器需要实现的方法集合
use rand::Rng;

fn print_hello_world() {
    println!("Hello, world!");
}

/// main函数（也称为主函数）很特殊，它始终是每个可执行Rust程序
/// 中运行的第一个代码。
fn main() {
    print_hello_world();

    println!("Guess the number!");

    // [1, 101)
    let secret_number = rand::thread_rng().gen_range(1..101);
    // println!("The secret number is: {}", secret_number);

    loop {
        println!("Please input your guess.");

        // String 内部使用UTF-8进行存储字符串编码
        // 此处利用了类型自动推导能力
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        // Rust 支持同名变量来隐藏旧变量的值 ==> 隐藏机制
        // let guess: u32 = guess.trim().parse().expect("Please type a number!");
        // 处理非法输入版本
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                // 在猜测成功时，优雅地退出
                break;
            }
        }
    }
}
