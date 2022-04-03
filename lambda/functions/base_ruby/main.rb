INIT_SLEEP = ENV['INIT_SLEEP'].to_i
HANDLER_SLEEP = ENV['HANDLER_SLEEP'].to_i

puts 'Init starting'
puts 'Sleep for %d second(s)' % [ INIT_SLEEP ]
sleep(INIT_SLEEP)
puts 'Init done'


def handler(event:, context:)
    puts 'Handler starting'
    puts 'Sleep for %d second(s)' % [ HANDLER_SLEEP ]
    sleep(HANDLER_SLEEP)
    puts 'Handler done'
end
