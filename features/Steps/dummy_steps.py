from behave import fixture, given, then, use_fixture, when

@given(u'a dummy given')
def step_impl(context):
    assert(True)


@when(u'a dummy thing happens')
def step_impl(context):
    assert(True)


@then(u'a dummy result happens too')
def step_impl(context):
    assert(True)