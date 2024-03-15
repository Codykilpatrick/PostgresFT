# How to get started
Download rust:
- https://rustup.rs/

Install dependencies with:
- `cargo build`

Install the cargo-pgrx sub-command with:
- `cargo install --locked cargo-pgrx`

Initialize the "PGRX Home" directory:
- `cargo pgrx init`

If this command fails you may need to run:
- `brew install icu4c`


## After that initializing pgrx:

In the my_extension directory:
- `cargo pgrx run`

This will drop us into psql where we can load the extension with:
- `CREATE EXTENSION my_extension;`


And test with:
- ````SELECT fft_example(ARRAY[0., 0.58778525,  0.95105652,  0.95105652,  0.58778525,  0., -0.58778525, -0.95105652, -0.95105652, -0.58778525, -0., 0.58778525,  0.95105652,  0.95105652,  0.58778525,  0., -0.58778525, -0.95105652, -0.95105652, -0.58778525]);````

