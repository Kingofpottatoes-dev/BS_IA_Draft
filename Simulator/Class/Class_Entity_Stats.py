
class Entity_stats:
    def __init__(
        self,
        Name,
        ItemName,
        WeaponSkill,
        UltimateSkill,
        OverchargedUltimateSkill,
        Pet,
        AltPet,
        Speed,
        Hitpoints,
        Traits,
        Components,
        HealthPromilleLostPerSecond,
        HealPercentChange,
        LifeTimeTicks,
        SkipDeploy,
        MeleeAutoAttackSplashDamage,
        DelayTicksFirstAttack,
        AutoAttackSpeedMs,
        AutoAttackDamage,
        AutoAttackBulletsPerShot,
        AutoAttackMode,
        AutoAttackTicksBetweenBurstShots,
        AutoAttackProjectileSpread,
        AutoAttackProjectile,
        OverchargedAutoAttackProjectile,
        AutoAttackRange,
        RegeneratePerSecond,
        LowPriorityTarget,
        UltiUses,
        UltiChargeInitial,
        UltiChargeMul,
        UltiChargeUltiMul,
        OverchargeChargeMul,
        OverchargePassiveChargeMul,
        OverchargeChargeActiveMul,
        OverchargeDamagePercent,
        OverchargeSpeedPercent,
        OverchargeShieldPercent,
        Type,
        IsNeutral,
        CarryableType,
        TwoWeaponAttackEffectOffset,
        CollisionRadius,
        ProjectileStartZ,
        AttackingWeaponScale,
        CanWalkOverWater,
        ChargeUltiAutomatically,
        ChargeUltiFromDamage,
        ChargeUltiFromHealing,
        ShouldEncodePetStatus,
        SecondaryPet,
        IsExternalPet,
        ExtraMinions,
        PetAutoSpawnDelay,
        PowerLevelsType,
        PowerLevelsSpeedBuff,
        UniqueProperty,
        UniquePropertyValue1,
        UniquePropertyValue2,
        BuddyCharacter,
        Texture
    ):
        self.Name = Name
        self.ItemName = ItemName
        self.WeaponSkill = WeaponSkill
        self.UltimateSkill = UltimateSkill
        self.OverchargedUltimateSkill = OverchargedUltimateSkill
        self.Pet = Pet
        self.AltPet = AltPet
        self.Speed = Speed
        self.Hitpoints = Hitpoints
        self.Traits = Traits
        self.Components = Components
        self.HealthPromilleLostPerSecond = HealthPromilleLostPerSecond
        self.HealPercentChange = HealPercentChange
        self.LifeTimeTicks = LifeTimeTicks
        self.SkipDeploy = SkipDeploy
        self.MeleeAutoAttackSplashDamage = MeleeAutoAttackSplashDamage
        self.DelayTicksFirstAttack = DelayTicksFirstAttack
        self.AutoAttackSpeedMs = AutoAttackSpeedMs
        self.AutoAttackDamage = AutoAttackDamage
        self.AutoAttackBulletsPerShot = AutoAttackBulletsPerShot
        self.AutoAttackMode = AutoAttackMode
        self.AutoAttackTicksBetweenBurstShots = AutoAttackTicksBetweenBurstShots
        self.AutoAttackProjectileSpread = AutoAttackProjectileSpread
        self.AutoAttackProjectile = AutoAttackProjectile
        self.OverchargedAutoAttackProjectile = OverchargedAutoAttackProjectile
        self.AutoAttackRange = AutoAttackRange
        self.RegeneratePerSecond = RegeneratePerSecond
        self.LowPriorityTarget = LowPriorityTarget
        self.UltiUses = UltiUses
        self.UltiChargeInitial = UltiChargeInitial
        self.UltiChargeMul = UltiChargeMul
        self.UltiChargeUltiMul = UltiChargeUltiMul
        self.OverchargeChargeMul = OverchargeChargeMul
        self.OverchargePassiveChargeMul = OverchargePassiveChargeMul
        self.OverchargeChargeActiveMul = OverchargeChargeActiveMul
        self.OverchargeDamagePercent = OverchargeDamagePercent
        self.OverchargeSpeedPercent = OverchargeSpeedPercent
        self.OverchargeShieldPercent = OverchargeShieldPercent
        self.Type = Type
        self.IsNeutral = IsNeutral
        self.CarryableType = CarryableType
        self.TwoWeaponAttackEffectOffset = TwoWeaponAttackEffectOffset
        self.CollisionRadius = CollisionRadius
        self.ProjectileStartZ = ProjectileStartZ
        self.AttackingWeaponScale = AttackingWeaponScale
        self.CanWalkOverWater = CanWalkOverWater
        self.ChargeUltiAutomatically = ChargeUltiAutomatically
        self.ChargeUltiFromDamage = ChargeUltiFromDamage
        self.ChargeUltiFromHealing = ChargeUltiFromHealing
        self.ShouldEncodePetStatus = ShouldEncodePetStatus
        self.SecondaryPet = SecondaryPet
        self.IsExternalPet = IsExternalPet
        self.ExtraMinions = ExtraMinions
        self.PetAutoSpawnDelay = PetAutoSpawnDelay
        self.PowerLevelsType = PowerLevelsType
        self.PowerLevelsSpeedBuff = PowerLevelsSpeedBuff
        self.UniqueProperty = UniqueProperty
        self.UniquePropertyValue1 = UniquePropertyValue1
        self.UniquePropertyValue2 = UniquePropertyValue2
        self.BuddyCharacter = BuddyCharacter
        self.Texture = Texture
    def __repr__(self):
        return f"<Brawler {self.ItemName} | HP={self.Hitpoints} | Speed={self.Speed}>"