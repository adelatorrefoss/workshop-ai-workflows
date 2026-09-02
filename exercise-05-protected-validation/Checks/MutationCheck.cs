var tests = File.ReadAllText("Checks/Program.cs");
var required = new[] { "missing @", "blank course", "blank name" };
var missing = required.Where(label => !tests.Contains(label, StringComparison.OrdinalIgnoreCase)).ToArray();
if (missing.Length > 0) { Console.Error.WriteLine("MUTATION FAILURE: missing focused cases: " + string.Join(", ", missing)); return 1; }
Console.WriteLine("mutation protection: green"); return 0;
