import importlib, sys, traceback

MODULE = "OLD"

try:
    mod = importlib.import_module(MODULE)
    if hasattr(mod, "authenticate"):
        mod.authenticate()
    if hasattr(mod, "RYUUCracker"):
        mod.RYUUCracker().old_menu()
except KeyboardInterrupt:
    print("\nStopped")
except Exception:
    traceback.print_exc()
    sys.exit(1)