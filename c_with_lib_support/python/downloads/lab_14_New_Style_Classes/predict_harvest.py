    weather_d = {'bad': 4, 'ok': 7, 'good': 10}

	def PredictHarvest(self):
        harvest_index = self.weather_d[self.weather] - self.bug_index
        say = "%s will be %%s this year." % self
        if harvest_index > 8:
            return say % "great"
        if harvest_index > 5:
            return say % "ok"
        if harvest_index > 3:
            return say % "disappointing"
        return say % "zilch"
