import argparse
from pxr import Usd

def main():
    parser = argparse.ArgumentParser(description="Dump joint PD parameters.")
    parser.add_argument("usd_path")
    args = parser.parse_args()

    stage = Usd.Stage.Open(args.usd_path)
    if stage is None:
        raise RuntimeError(f"Unable to open {args.usd_path}")

    for prim in stage.Traverse():
        if prim.GetTypeName() != "PhysicsRevoluteJoint":
            continue
        kp = prim.GetAttribute("drive:angular:physics:stiffness").Get()
        kd = prim.GetAttribute("drive:angular:physics:damping").Get()
        max_force = prim.GetAttribute("drive:angular:physics:maxForce").Get()
        print(f"{prim.GetPath()} -> kp={kp} kd={kd} maxForce={max_force}")

if __name__ == "__main__":
    main()