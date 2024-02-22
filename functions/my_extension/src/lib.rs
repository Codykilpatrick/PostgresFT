use pgrx::prelude::*;
use rustfft::{FftPlanner, num_complex::Complex};

pgrx::pg_module_magic!();

#[pg_extern]
fn hello_my_extension() -> &'static str {
    "Hello, my_extension"
}

#[cfg(any(test, feature = "pg_test"))]
#[pg_schema]
mod tests {
    use pgrx::prelude::*;

    #[pg_test]
    fn test_hello_my_extension() {
        assert_eq!("Hello, my_extension", crate::hello_my_extension());
    }

}

/// This module is required by `cargo pgrx test` invocations.
/// It must be visible at the root of your extension crate.
#[cfg(test)]
pub mod pg_test {
    pub fn setup(_options: Vec<&str>) {
        // perform one-off initialization when the pg_test framework starts
    }

    pub fn postgresql_conf_options() -> Vec<&'static str> {
        // return any postgresql.conf settings that are required for your tests
        vec![]
    }
}

#[pg_extern]
fn fft_example(input: Vec<f64>) -> Vec<f64> {
    let mut input_complex: Vec<Complex<f64>> = input.into_iter().map(Complex::from).collect();
    let mut planner = FftPlanner::<f64>::new();
    let fft = planner.plan_fft_forward(input_complex.len());
    fft.process(&mut input_complex);
    
    // Extract and round the imaginary parts to 5 decimal places
    input_complex.into_iter().map(|c| (c.im * 1000.0).round() / 1000.0).collect()
}


#[cfg(any(test, feature = "pg_test"))]
mod tests {
    use super::*;

    #[pg_test]
    fn test_hello_fourier_transform() {
        assert_eq!("Hello, fourier_transform", hello_fourier_transform());
    }

    // Add tests for fft_example as needed
}

// Required module for `cargo pgx test`
#[cfg(test)]
pub mod pg_test {
    pub fn setup(_options: Vec<&str>) {}
    pub fn postgresql_conf_options() -> Vec<&'static str> { vec![] }
}
