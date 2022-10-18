#[derive(Debug)]
pub struct HighScores<'a> {
    data: &'a [u32],
}

impl<'a> HighScores<'a> {
    pub fn new(scores: &'a [u32]) -> Self {
        Self { data: scores }
    }

    pub fn scores(&self) -> &[u32] {
        self.data
    }

    pub fn latest(&self) -> Option<u32> {
        self.data.last().copied()
    }

    pub fn personal_best(&self) -> Option<u32> {
        self.data.iter().max().copied()
    }

    pub fn personal_top_three(&self) -> Vec<u32> {
        let mut as_vec = self.data.to_vec();
        as_vec.sort_by(|a, b| b.cmp(a));
        as_vec.truncate(3);

        as_vec
    }
}
