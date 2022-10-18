const FULL_LIFE: u32 = 100;
const FULL_MANA: u32 = 100;

pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    fn new(mana: Option<u32>, level: u32) -> Self {
        Self {
            health: FULL_LIFE,
            mana: mana.map(|_| FULL_MANA),
            level,
        }
    }

    pub fn revive(&self) -> Option<Player> {
        (self.health == 0).then(|| Self::new(self.mana, self.level))
    }

    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 {
        match self.mana {
            Some(v) => {
                if v < mana_cost {
                    return 0;
                }
                self.mana = Some(v - mana_cost);
                mana_cost * 2
            }
            None => {
                self.health -= std::cmp::min(mana_cost, self.health);
                0
            }
        }
    }
}
