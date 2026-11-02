from pathlib import Path
import importlib.util
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("withdrawal_tests",R/"skills/quaderno-accessibile/tests/test_ritiro_documento.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
WithdrawalTests=m.WithdrawalTests
