class ProjectileConfig:
    def __init__(
        self,
        Name,
        Disabled,
        Speed,
        PreExplosionTimeMs,
        Radius,
        IgnoreCloseWalls,
        Indirect,
        ConstantFlyTime,
        TriggerWithDelayMs,
        BouncePercent,
        Gravity,
        EarlyTicks,
        OnAllyHitActions,
        OnEnemyHitActions,
        AreaEffect2DamagePercent,
        SpawnCharacter,
        AreaEffectTrailMinDistance,
        ShotByHero,
        IsBeam,
        IsBouncing,
        DistanceAddFromBounce,
        MaxDistanceBounces,
        PiercesCharacters,
        PiercesEnvironment,
        PiercesEnvironmentLikeButter,
        PushbackStrength,
        PushbackType,
        OverridePushbackSpeed,
        MaxZDuringPushback,
        ChainsToEnemies,
        ChainBullets,
        ChainBulletsMax,
        ChainSpread,
        ChainTravelDistance,
        ExecuteChainSpecialCase,
        DamagePercentStart,
        DamagePercentEnd,
        DamageChangeStartPromille,
        DamageChangeEndPromille,
        IgnoreDamageChangeForUltiCharge,
        DamagesConstantlyTickDelay,
        FreezeStrength,
        FreezeDurationMS,
        StunLengthMS,
        PartialStunPromille,
        SilenceDurationMS,
        ScaleStart,
        ScaleEnd,
        AttractsPet,
        LifeStealPercent,
        PassesEnvironment,
        SuppressHealing,
        SuppressHealingTicks,
        ConsumableShield,
        ConsumableShieldTicks,
        DamageOnlyWithOneProj,
        HealOwnPercent,
        GrapplesEnemy,
        KickBack,
        MinDistanceForSpread,
        IsFriendlyHomingMissile,
        BoomerangType,
        CanHitAgainAfterBounce,
        IsHomingMissile,
        UltiChargeChangePercent,
        TravelType,
        TravelTypeVariable,
        TravelTypeVariable2,
        IgnoreLevelBorder,
        SteerStrength,
        SteerIgnoreTicks,
        HomeDistance,
        SteerLifeTime,
        DoNotForceShow,
        UniqueProperty,
        CustomUniquePropertyValue,
        Zoffset
    ):
        self.Name = Name
        self.Disabled = Disabled
        self.Speed = Speed
        self.PreExplosionTimeMs = PreExplosionTimeMs
        self.Radius = Radius
        self.IgnoreCloseWalls = IgnoreCloseWalls
        self.Indirect = Indirect
        self.ConstantFlyTime = ConstantFlyTime
        self.TriggerWithDelayMs = TriggerWithDelayMs
        self.BouncePercent = BouncePercent
        self.Gravity = Gravity
        self.EarlyTicks = EarlyTicks
        self.OnAllyHitActions = OnAllyHitActions
        self.OnEnemyHitActions = OnEnemyHitActions
        self.AreaEffect2DamagePercent = AreaEffect2DamagePercent
        self.SpawnCharacter = SpawnCharacter
        self.AreaEffectTrailMinDistance = AreaEffectTrailMinDistance
        self.ShotByHero = ShotByHero
        self.IsBeam = IsBeam
        self.IsBouncing = IsBouncing
        self.DistanceAddFromBounce = DistanceAddFromBounce
        self.MaxDistanceBounces = MaxDistanceBounces
        self.PiercesCharacters = PiercesCharacters
        self.PiercesEnvironment = PiercesEnvironment
        self.PiercesEnvironmentLikeButter = PiercesEnvironmentLikeButter
        self.PushbackStrength = PushbackStrength
        self.PushbackType = PushbackType
        self.OverridePushbackSpeed = OverridePushbackSpeed
        self.MaxZDuringPushback = MaxZDuringPushback
        self.ChainsToEnemies = ChainsToEnemies
        self.ChainBullets = ChainBullets
        self.ChainBulletsMax = ChainBulletsMax
        self.ChainSpread = ChainSpread
        self.ChainTravelDistance = ChainTravelDistance
        self.ExecuteChainSpecialCase = ExecuteChainSpecialCase
        self.DamagePercentStart = DamagePercentStart
        self.DamagePercentEnd = DamagePercentEnd
        self.DamageChangeStartPromille = DamageChangeStartPromille
        self.DamageChangeEndPromille = DamageChangeEndPromille
        self.IgnoreDamageChangeForUltiCharge = IgnoreDamageChangeForUltiCharge
        self.DamagesConstantlyTickDelay = DamagesConstantlyTickDelay
        self.FreezeStrength = FreezeStrength
        self.FreezeDurationMS = FreezeDurationMS
        self.StunLengthMS = StunLengthMS
        self.PartialStunPromille = PartialStunPromille
        self.SilenceDurationMS = SilenceDurationMS
        self.ScaleStart = ScaleStart
        self.ScaleEnd = ScaleEnd
        self.AttractsPet = AttractsPet
        self.LifeStealPercent = LifeStealPercent
        self.PassesEnvironment = PassesEnvironment
        self.SuppressHealing = SuppressHealing
        self.SuppressHealingTicks = SuppressHealingTicks
        self.ConsumableShield = ConsumableShield
        self.ConsumableShieldTicks = ConsumableShieldTicks
        self.DamageOnlyWithOneProj = DamageOnlyWithOneProj
        self.HealOwnPercent = HealOwnPercent
        self.GrapplesEnemy = GrapplesEnemy
        self.KickBack = KickBack
        self.MinDistanceForSpread = MinDistanceForSpread
        self.IsFriendlyHomingMissile = IsFriendlyHomingMissile
        self.BoomerangType = BoomerangType
        self.CanHitAgainAfterBounce = CanHitAgainAfterBounce
        self.IsHomingMissile = IsHomingMissile
        self.UltiChargeChangePercent = UltiChargeChangePercent
        self.TravelType = TravelType
        self.TravelTypeVariable = TravelTypeVariable
        self.TravelTypeVariable2 = TravelTypeVariable2
        self.IgnoreLevelBorder = IgnoreLevelBorder
        self.SteerStrength = SteerStrength
        self.SteerIgnoreTicks = SteerIgnoreTicks
        self.HomeDistance = HomeDistance
        self.SteerLifeTime = SteerLifeTime
        self.DoNotForceShow = DoNotForceShow
        self.UniqueProperty = UniqueProperty
        self.CustomUniquePropertyValue = CustomUniquePropertyValue
        self.Zoffset = Zoffset