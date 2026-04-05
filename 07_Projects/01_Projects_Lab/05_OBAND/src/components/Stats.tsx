"use client";

import { motion } from "framer-motion";
import { Building2, Users, Award, Clock } from "lucide-react";

const STATS = [
  { icon: Building2, value: "150+", label: "Projects Delivered" },
  { icon: Users, value: "8+", label: "Years Experience" },
  { icon: Award, value: "98%", label: "Client Satisfaction" },
  { icon: Clock, value: "500+", label: "Spaces Optimized" },
];

const springTransition = {
  type: "spring" as const,
  stiffness: 300,
  damping: 30,
};

export default function Stats() {
  return (
    <section className="w-full py-24 px-6 md:px-8 bg-glass/5 border-y border-glass-border">
      <div className="max-w-7xl mx-auto">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8 md:gap-12">
          {STATS.map((stat, i) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ ...springTransition, duration: 0.6, delay: i * 0.1 }}
              className="flex flex-col items-center text-center"
            >
              <div className="p-3 bg-accent/10 rounded-2xl mb-4">
                <stat.icon className="w-6 h-6 text-accent" />
              </div>
              <span className="text-4xl md:text-5xl font-bold font-heading text-white mb-2">
                {stat.value}
              </span>
              <span className="text-sm text-muted uppercase tracking-widest">
                {stat.label}
              </span>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}