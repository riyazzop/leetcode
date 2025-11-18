class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        for a in asteroids:
            if a>mass:
                return False
            mass+=a
        return True
        