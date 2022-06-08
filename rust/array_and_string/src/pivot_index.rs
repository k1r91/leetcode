pub struct Solution {

}

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
}