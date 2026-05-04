import Link from "next/link";

const navItems = [
  { label: "Home", href: "/" },
  { label: "About the Book", href: "#about" },
  { label: "Examples", href: "#examples" },
  { label: "Resources", href: "#resources" },
  { label: "Contact", href: "#contact" },
];

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      {/* Navigation */}
      <nav className="border-b border-slate-700/50 backdrop-blur-sm bg-slate-900/80 sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <span className="text-sm font-mono font-semibold text-amber-400 tracking-wide">
            PythonforPLAXIS
          </span>
          <ul className="hidden md:flex items-center gap-8">
            {navItems.map((item) => (
              <li key={item.label}>
                <Link
                  href={item.href}
                  className="text-sm text-slate-400 hover:text-white transition-colors"
                >
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
          <a
            href="https://github.com/geotechscripting/PythonforPLAXIS"
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm text-slate-400 hover:text-white transition-colors"
          >
            GitHub
          </a>
        </div>
      </nav>

      {/* Hero */}
      <main className="flex-1 flex flex-col items-center justify-center px-6">
        <div className="max-w-3xl mx-auto text-center space-y-8 -mt-16">
          {/* Construction badge */}
          <div className="inline-flex items-center gap-2 rounded-full border border-amber-500/30 bg-amber-500/10 px-4 py-1.5">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-amber-400"></span>
            </span>
            <span className="text-xs font-medium text-amber-300 tracking-wide uppercase">
              Under Construction
            </span>
          </div>

          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-white leading-tight">
            Python Scripting
            <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-500">
              in PLAXIS
            </span>
          </h1>

          <p className="text-lg sm:text-xl text-slate-400 max-w-2xl mx-auto leading-relaxed">
            Automating Geotechnical Analysis and Modelling Workflows
          </p>

          <div className="w-16 h-px bg-gradient-to-r from-transparent via-slate-600 to-transparent mx-auto"></div>

          <p className="text-sm text-slate-500 max-w-lg mx-auto">
            Companion website for the book. Code examples, resources, and
            documentation coming soon.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
            <a
              href="https://github.com/geotechscripting/PythonforPLAXIS"
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-lg bg-white text-slate-900 px-6 py-3 text-sm font-semibold hover:bg-slate-200 transition-colors"
            >
              View on GitHub
            </a>
            <span className="rounded-lg border border-slate-700 px-6 py-3 text-sm text-slate-500 cursor-default">
              Book &mdash; Coming Soon
            </span>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-800 py-6 text-center text-xs text-slate-600">
        &copy; {new Date().getFullYear()} geotechscripting
      </footer>
    </div>
  );
}
