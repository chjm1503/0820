#[no_mangle]
pub extern "C" fn hello_world() {
    println!("Hello, world!");
}

/// 以下是cargo创建新项目默认生成的示例代码
pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
