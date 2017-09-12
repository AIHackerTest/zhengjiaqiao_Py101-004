print("Let's practice everything.")
print('You\'d need to konw \' about escapes with \\ that do \n newlines and \t tabs.')

poem ="""
\tThe lovely world with logic so firmly planted cannot discrern \n the need of love
not comptehend passin frome intuition
and requites an explannation \n\twhere there is none."""

print("-" * 14)
print(poem)
print("-" * 14)

five =10-2+3-6
print("This should be five:%s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of :%d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars,crates))

start_point = start_point / 10

print("We'd have %d beans , %d jars and %d crates." % secret_formula(start_point))
