def test_package_imports():
    import ai_arsenal as aa

    assert callable(aa.main)
