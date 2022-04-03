#[macro_use]
extern crate lambda_runtime as lambda;
extern crate lazy_static;

#[macro_use]
extern crate serde_derive;
extern crate simple_logger;

use lambda::error::HandlerError;
use lazy_static::lazy_static;

use std::env::var;
use std::error::Error;
use std::{thread, time};

#[derive(Deserialize, Clone)]
struct CustomEvent {}

lazy_static! {
    static ref INIT_SLEEP: u64 = var("INIT_SLEEP").unwrap().parse::<u64>().unwrap();
    static ref HANDLER_SLEEP: u64 = var("HANDLER_SLEEP").unwrap().parse::<u64>().unwrap();
}

fn main() -> Result<(), Box<dyn Error>> {
    println!("Init starting");
    println!("Sleep for {} second(s)", *INIT_SLEEP);
    thread::sleep(time::Duration::from_secs(*INIT_SLEEP));
    println!("Init done");
    lambda!(my_handler);

    Ok(())
}

fn my_handler(_: CustomEvent, _: lambda::Context) -> Result<(), HandlerError> {
    println!("Handler starting");
    println!("Sleep for {} second(s)", *HANDLER_SLEEP);
    thread::sleep(time::Duration::from_secs(*HANDLER_SLEEP));
    println!("Handler done");

    Ok(())
}
