pub struct Solution {}

impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let mut left_sum: i32 = 0;
        let mut right_sum: i32 = 0;
        let length: usize = nums.len();
        for i in 1..length {
            right_sum += nums[i];
        }
        for i in 0..length - 1 {
            if left_sum == right_sum {
                return i as i32;
            }
            left_sum += nums[i];
            right_sum -= nums[i + 1];
        }
        if left_sum == 0 {
            return { length - 1 } as i32;
        }
        return -1;
    }
    pub fn dominant_index(nums: Vec<i32>) -> i32 {
        let len = nums.len();
        if nums.len() == 1 {
            return 0;
        }
        let mut index_max: usize = 0;
        for i in 0..len {
            if nums[index_max] < nums[i] {
                index_max = i;
            }
        }
        for i in 0..len {
            if nums[i] != nums[index_max] && nums[i] * 2 > nums[index_max] {
                return -1;
            }
        }
        return index_max as i32;
    }
}

pub fn test_dominant_index() {
    let nums = vec![0, 0, 0, 1];
    println!("{}", Solution::dominant_index(nums) == 3);
    let nums = vec![3, 6, 1, 0];
    println!("{}", Solution::dominant_index(nums) == 1);
    let nums = vec![1, 2, 3, 4];
    println!("{}", Solution::dominant_index(nums) == -1);
    let nums = vec![1];
    println!("{}", Solution::dominant_index(nums) == 0);
}

pub fn test_pivot_index() {
    let nums = vec![1, 2, 3];
    println!("{}", Solution::pivot_index(nums) == -1);
    let nums = vec![1, 7, 3, 6, 5, 6];
    println!("{}", Solution::pivot_index(nums) == 3);
    let nums = vec![2, 1, -1];
    println!("{}", Solution::pivot_index(nums) == 0);
}
