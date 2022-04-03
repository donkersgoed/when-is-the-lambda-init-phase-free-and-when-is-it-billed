rm -rf function.zip
rustup target add x86_64-unknown-linux-musl
brew install filosottile/musl-cross/musl-cross
mkdir .cargo
echo '[target.x86_64-unknown-linux-musl]
linker = "x86_64-linux-musl-gcc"' > .cargo/config
cargo build --release --target x86_64-unknown-linux-musl
zip -j function.zip ./target/x86_64-unknown-linux-musl/release/bootstrap
