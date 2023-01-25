import vsketch


class DebugCircleSketch(vsketch.SketchClass):
    # Sketch parameters:
    radius_in_inches = vsketch.Param(1.0)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("12inx12in", landscape=True)
        vsk.scale("in")

        # implement your sketch here
        # vsk.circle(0, 0, self.radius, mode="radius")
        x = 0
        vsk.stroke(1)
        vsk.circle(x, 0, radius=self.radius_in_inches)

        vsk.line(x, 0, x + self.radius_in_inches, 0)

        x += 4 * self.radius_in_inches

        vsk.stroke(2)
        vsk.circle(x, 0, radius=self.radius_in_inches, mode="radius")
        vsk.line(x, 0, x + self.radius_in_inches, 0)
        x += 4 * self.radius_in_inches

        vsk.ellipseMode("radius")

        vsk.stroke(3)
        vsk.circle(8 * self.radius_in_inches, 0, radius=self.radius_in_inches)
        vsk.line(x, 0, x + self.radius_in_inches, 0)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    DebugCircleSketch.display()
