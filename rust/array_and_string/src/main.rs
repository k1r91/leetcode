mod pivot_index;

fn main() {
    let nums= vec![1, 2, 3];
    println!("{}", pivot_index::Solution::pivot_index(nums));
    let nums= vec![1,7,3,6,5,6];
    println!("{}", pivot_index::Solution::pivot_index(nums));
    let nums= vec![2,1,-1];
    println!("{}", pivot_index::Solution::pivot_index(nums));
}
