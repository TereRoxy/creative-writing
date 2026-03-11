import math
import time
# "All in all you're just another brick in the wall" - PF
# "Money, money, money, must be funny, in the rich man's world" - ABBA

planck_constant = 6.62607015e-34     # the fundamental constant of nature

class Light():
    """
    The Nature of the energy is the same, the manifestation depends on the instantiation 
    """
    def __init__(self, frequency):
        self.energy = planck_constant * frequency
        self.is_wave = True     # the infinite possibilities of existance
        self.is_particle = True     # the discrete reality of The Algorithm

    # "Conversion, software version 7.0" - SOAD
    def refraction(self, prism_angle):
        """
        sin(theta) = n2/n1 * sin(prism_angle)
        where n1 is the index of refraction of the medium the light is coming from
        if the angle of refraction is greater than the critical angle, the light will be totally internally reflected, otherwise it will be refracted according to Snell's law
        """
        n1 = 1.0
        n2 = self.index_of_refraction
        try:
            if not self.is_observed:
                return "The light is not observed, it cannot be refracted or reflected, transparent to the observer"
            
            sin_theta = n2 / n1 * math.sin(math.radians(prism_angle))
            if sin_theta > 1:
                return "The light is totally internally reflected, it cannot be refracted, it is reflected back into the medium"
            else:
                angle_out = math.degrees(math.asin(sin_theta))
                return f"The light is refracted at an angle of {angle_out} degrees. Another brick in the rainbow wall"
            
        except Exception as e:
            print(f"An error occurred: {e}.")
            return "Error: The wave function collapsed"
        

class UV(Light):
    """
    The ultraviolet light has the highest energy and the shortest wavelength, it can cause damage to living organisms
    """
    def __init__(self, frequency=7.5e14): # the frequency of ultraviolet light          -- "The sharpest lives are the deadliest to lead \n A light to burn all the empires \n So bright, the sun is ashamed to rise and be " - My Chemical Romance
        super().__init__(frequency)     
        self.index_of_refraction = 1.0     # the bending of reality
        self.is_visible = False     # the invisible nature
        self.is_observed = False    # The preservation of the wave function

class Visible(Light):
    """
    The visible light is the range of frequencies that can be perceived by the human eye, it is what we interact with daily
    """
    def __init__(self, frequency=5e14): # the frequency of visible light    -- "Never let them take the light behind your eyes" -- MCR
        super().__init__(frequency)  
        self.index_of_refraction = 1.33      
        self.is_visible = True     # the visible nature
        self.is_observed = True     # the act of observation collapses the wave function, observed as color and light

class Infrared(Light):
    """
    The infrared light has the lowest energy and the longest wavelength, it is the heat that we feel, but mostly ignore
    """
    def __init__(self, frequency=1e12): # the frequency of infrared light    -- "I'm going under \n Drowning in you \n I'm falling forever" -- Evanescence
        super().__init__(frequency)  
        self.index_of_refraction = 1.5   
        self.is_visible = False     # the invisible nature
        self.is_observed = True     # the act of observation collapses the wave function, observed as heat

# 

def main():
    population = {
        "UV": [UV() for _ in range(1)], # 1%, High Energy Architects of the Prism
        "Visible": [Visible() for _ in range(9)], # 9% - The Refracted Norm
        "Infrared": [Infrared() for _ in range(90)] # 90% - The Hidden Heat
    }

    the_prism_angle = 45.0  # the angle of the prism, the angle of reality bending
    print("\nTHE NEW SYSTEM CYCLE LIGHT SHOW BEGINS:\n")

    for light_type, light_population in population.items():
        print(f"\n{light_type} Light: {len(light_population)} instances")
        print("The light interacts with the prism. The fate of the light is determined...")
        for light in light_population:
            result = light.refraction(the_prism_angle)
            print(result)

    print("\n The show has to continue, the cycle of light and shadow, the dance of energy and matter, the eternal spectacle of existence unfolds again and again\n")
    time.sleep(5)  # a pause to the show for the observer to take in the spectacle

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:

        print("\nThe system cycle light show has been interrupted. The observer has left the stage. The wave function returns to chaos\n")
