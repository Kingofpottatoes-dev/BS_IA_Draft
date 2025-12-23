class Brawler:
    def __init__(
        self,
        name,
        weapon_skill,
        ultimate_skill,
        overcharged_ultimate_skill,
        movement_type,
        speed,
        hitpoints,
        collision_radius,
        flying_height,
        auto_attack_damage,
        auto_attack_bullets_per_shot,
        auto_attack_speed_ms,
        auto_attack_range,
        auto_attack_projectile,
        overcharged_auto_attack_projectile,
        auto_attack_projectile_spread,
        auto_attack_mode,
        auto_attack_ticks_between_burst_shots,
        delay_ticks_first_attack,
        regenerate_per_second,
        stop_movement_after_ms,
        wait_ms,
        ulti_uses,
        ulti_charge_initial,
        ulti_charge_mul,
        ulti_charge_ulti_mul,
        charge_ulti_automatically,
        charge_ulti_from_damage,
        charge_ulti_from_healing,
        overcharge_damage_percent,
        overcharge_speed_percent,
        overcharge_shield_percent,
        overcharge_charge_mul,
        class_archetype,
        type_
    ):
        self.name = name
        self.weapon_skill = weapon_skill
        self.ultimate_skill = ultimate_skill
        self.overcharged_ultimate_skill = overcharged_ultimate_skill
        self.movement_type = movement_type
        self.speed = float(speed)
        self.hitpoints = float(hitpoints)
        self.collision_radius = float(collision_radius)
        self.flying_height = float(flying_height)

        # Auto-attack
        self.auto_attack_damage = float(auto_attack_damage)
        self.auto_attack_bullets_per_shot = int(auto_attack_bullets_per_shot)
        self.auto_attack_speed_ms = int(auto_attack_speed_ms)
        self.auto_attack_range = float(auto_attack_range)
        self.auto_attack_projectile = auto_attack_projectile
        self.overcharged_auto_attack_projectile = overcharged_auto_attack_projectile
        self.auto_attack_projectile_spread = float(auto_attack_projectile_spread)
        self.auto_attack_mode = auto_attack_mode
        self.auto_attack_ticks_between_burst_shots = int(auto_attack_ticks_between_burst_shots)
        self.delay_ticks_first_attack = int(delay_ticks_first_attack)

        # Ulti / Regeneration
        self.regenerate_per_second = float(regenerate_per_second)
        self.stop_movement_after_ms = float(stop_movement_after_ms)
        self.wait_ms = float(wait_ms)
        self.ulti_uses = int(ulti_uses)
        self.ulti_charge_initial = float(ulti_charge_initial)
        self.ulti_charge_mul = float(ulti_charge_mul)
        self.ulti_charge_ulti_mul = float(ulti_charge_ulti_mul)
        self.charge_ulti_automatically = bool(int(charge_ulti_automatically))
        self.charge_ulti_from_damage = bool(int(charge_ulti_from_damage))
        self.charge_ulti_from_healing = bool(int(charge_ulti_from_healing))

        # Overcharge
        self.overcharge_damage_percent = float(overcharge_damage_percent)
        self.overcharge_speed_percent = float(overcharge_speed_percent)
        self.overcharge_shield_percent = float(overcharge_shield_percent)
        self.overcharge_charge_mul = float(overcharge_charge_mul)

        # Classification
        self.class_archetype = class_archetype
        self.type_ = type_

        # État runtime
        self.current_hp = self.hitpoints
        self.ulti_charge = self.ulti_charge_initial
        self.position = (0.0, 0.0)  # x, y float
        self.is_alive = True

    def __repr__(self):
        return f"<Brawler {self.name} HP:{self.current_hp} Pos:{self.position}>"