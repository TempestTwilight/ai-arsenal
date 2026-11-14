def test_package_imports() -> None:
    import ai_arsenal as aa

    assert callable(aa.main)
