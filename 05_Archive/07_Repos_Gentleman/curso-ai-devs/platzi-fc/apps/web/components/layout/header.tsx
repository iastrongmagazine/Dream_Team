"use client";

import Link from "next/link";
import { useState } from "react";
import { Menu, X, Search, ChevronDown } from "lucide-react";
import { mainNav, type NavItem } from "./nav-data";
import { cn } from "@/lib/utils/cn";

function DesktopNavItem({ item }: { item: NavItem }) {
  const [open, setOpen] = useState(false);

  if (!item.children) {
    return (
      <Link
        href={item.href}
        className="px-3 py-2 text-sm font-medium text-white/90 hover:text-white transition-colors"
      >
        {item.label}
      </Link>
    );
  }

  return (
    <div
      className="relative"
      onMouseEnter={() => setOpen(true)}
      onMouseLeave={() => setOpen(false)}
    >
      <button
        className="inline-flex items-center gap-1 px-3 py-2 text-sm font-medium text-white/90 hover:text-white transition-colors"
        aria-expanded={open}
      >
        {item.label}
        <ChevronDown className={cn("h-3.5 w-3.5 transition-transform", open && "rotate-180")} />
      </button>
      {open && (
        <div className="absolute left-0 top-full z-50 min-w-[200px] rounded-md border border-white/10 bg-primary-dark p-1 shadow-lg">
          {item.children.map((child) => (
            <Link
              key={child.href}
              href={child.href}
              className="block rounded-sm px-3 py-2 text-sm text-white/80 hover:bg-white/10 hover:text-white transition-colors"
            >
              {child.label}
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}

function MobileNav({
  open,
  onClose,
}: {
  open: boolean;
  onClose: () => void;
}) {
  const [expanded, setExpanded] = useState<string | null>(null);

  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 lg:hidden">
      <div className="fixed inset-0 bg-black/60" onClick={onClose} />
      <nav className="fixed inset-y-0 left-0 w-[300px] overflow-y-auto bg-primary-dark p-6">
        <div className="mb-8 flex items-center justify-between">
          <span className="text-lg font-bold text-white">Platzi FC</span>
          <button onClick={onClose} aria-label="Cerrar menú">
            <X className="h-6 w-6 text-white" />
          </button>
        </div>
        <ul className="space-y-1">
          {mainNav.map((item) => (
            <li key={item.href}>
              {item.children ? (
                <>
                  <button
                    className="flex w-full items-center justify-between rounded-md px-3 py-2.5 text-sm font-medium text-white/90 hover:bg-white/10"
                    onClick={() =>
                      setExpanded(expanded === item.label ? null : item.label)
                    }
                  >
                    {item.label}
                    <ChevronDown
                      className={cn(
                        "h-4 w-4 transition-transform",
                        expanded === item.label && "rotate-180"
                      )}
                    />
                  </button>
                  {expanded === item.label && (
                    <ul className="ml-4 space-y-1 border-l border-white/10 pl-3">
                      {item.children.map((child) => (
                        <li key={child.href}>
                          <Link
                            href={child.href}
                            className="block rounded-md px-3 py-2 text-sm text-white/70 hover:bg-white/10 hover:text-white"
                            onClick={onClose}
                          >
                            {child.label}
                          </Link>
                        </li>
                      ))}
                    </ul>
                  )}
                </>
              ) : (
                <Link
                  href={item.href}
                  className="block rounded-md px-3 py-2.5 text-sm font-medium text-white/90 hover:bg-white/10"
                  onClick={onClose}
                >
                  {item.label}
                </Link>
              )}
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
}

export function Header() {
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 w-full border-b border-white/10 bg-primary">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-2">
          <div className="flex h-9 w-9 items-center justify-center rounded-full bg-secondary text-primary-dark font-bold text-sm">
            PFC
          </div>
          <span className="hidden text-lg font-bold text-white sm:block">
            Platzi FC
          </span>
        </Link>

        {/* Desktop Nav */}
        <nav className="hidden lg:flex lg:items-center lg:gap-0.5" aria-label="Navegación principal">
          {mainNav.map((item) => (
            <DesktopNavItem key={item.href} item={item} />
          ))}
        </nav>

        {/* Actions */}
        <div className="flex items-center gap-2">
          <Link
            href="/busqueda"
            className="rounded-md p-2 text-white/80 hover:bg-white/10 hover:text-white transition-colors"
            aria-label="Buscar"
          >
            <Search className="h-5 w-5" />
          </Link>
          <button
            className="rounded-md p-2 text-white/80 hover:bg-white/10 hover:text-white transition-colors lg:hidden"
            onClick={() => setMobileOpen(true)}
            aria-label="Abrir menú"
          >
            <Menu className="h-5 w-5" />
          </button>
        </div>
      </div>

      <MobileNav open={mobileOpen} onClose={() => setMobileOpen(false)} />
    </header>
  );
}
