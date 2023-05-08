live_loop :flibble do
  sample :bd_haus, rate: 1
  sleep 1
end


live_loop :flibble do
  play_pattern chord(:E3, :M7)
  sleep 1
end


live_loop :test1 do
  use_real_time
  a, b, c = sync "/osc*/trigger/prophet"
  synth :prophet, note: a, cutoff: b, sustain: c
end


live_loop :test2 do
  use_real_time
  a, b, c = sync "/osc*/trigger/pulse"
  synth :pulse, note: 64, cutoff: b, sustain: c
end



