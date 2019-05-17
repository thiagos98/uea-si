var targettext = 'METHINKS IT IS A WEASEL';
            var allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ";

            function mutate(string, mutation_rate) {
                var result = "";
                for (var i=0; i < string.length; i++) {
                    var new_char;
                    if (Math.random() < mutation_rate) {
                        result += get_random_char();
                    } else {
                        result += string[i];
                    }
                }
                return result;
            }

            function mutation_set(string, target, generation_size, mutation_rate) {
                var best_score = -1;
                var best_string = '';
                for (var i=0; i < generation_size; i++) {
                    var new_string = mutate(string, mutation_rate);
                    var new_score = compute_score(new_string, target);
                    if (new_score > best_score) {
                        best_score = new_score;
                        best_string = new_string;
                    }
                }
                return best_string;
            }

            function do_many(target, n) {
                counts = [];
                for (var i = 0; i < n; i++) {
                    counts.push(do_analysis(target));
                }
                return counts;
            }

            function plot_many(target, n) {
                var start_time = (new Date).getTime();
                var data = [['','']];
                var counts = do_many(target, n);

                // ensures the boxes appear in a reasonable order on the stack
                // in the histogram
                counts.sort();

                for (var i = 0; i < n; i++) {
                    data.push(['', counts[i]]);
                }
                var end_time = (new Date).getTime();
                data = google.visualization.arrayToDataTable(data);
                var options = {
                    title: 'n = ' + n + ' simulations in ' + (end_time - start_time) / 1000. + 's; mean = ' + average(counts),
                    hAxis: {title: 'Generations to evolve: ' + target.toUpperCase()},
                    legend: { position: 'none' },
                };
                var chart = new google.visualization.Histogram(document.getElementById('histogram'));
                chart.draw(data, options);
            }

            function average(items) {
                sum = 0.;
                for (var i = 0; i < items.length; i++) {
                    sum += items[i];
                }
                return sum / items.length;
            }

            // getting a random string modified from
            // http://stackoverflow.com/questions/1349404/generate-a-string-of-5-random-characters-in-javascript
            function makeid(length) {
                var text = "";
                for (var i=0; i < length; i++) {
                    text += get_random_char();
                }
                return text;
            }
            function get_random_char() {
                return allowed_chars.charAt(Math.floor(Math.random() * allowed_chars.length));
            }

            function do_analysis(target) {
                target = target.toUpperCase();
                var table = $('#generations');
                table.html('<tr><th>Generation</th><th>Phrase</th><th>Score</th></tr>');
                var string = makeid(target.length);
                var score = compute_score(string, target);
                var generation_size = $("#generationspinner").val();
                var mutation_rate = $("#mutationspinner").val() * 0.01;
                table.append(generation_row(0, string, score, target));
                var i = 0;
                while (score < target.length) {
                    string = mutation_set(string, target, generation_size, mutation_rate);
                    score = compute_score(string, target);
                    i += 1;
                    table.append(generation_row(i, string, score, target));
                }
                return i;
            }

            function generation_row(generation, string, score, target) {
                // highlight mismatches
                var highlighted_string = '';
                var inside_error = false;
                for (var i = 0; i < target.length; i++) {
                    if (target[i] != string[i]) {
                        if (!inside_error) {
                            inside_error = true;
                            highlighted_string += '<span class="err">';
                        }
                    } else if (inside_error) {
                        inside_error = false;
                        highlighted_string += '</span>';
                    }
                    highlighted_string += string[i];
                }
                if (inside_error) {
                    highlighted_string += '</span>';
                }
                // TODO: highlight matches
                return "<tr><td style='width:5em'>" + generation + "</td><td style='width:25em' class='monospace'>" + highlighted_string + "</td><td width='5em'>" + score + "</td>";
            }

            function compute_score(test, target) {
                var score = 0;
                for (var i=0; i<target.length; i++) {
                    if (test[i] == target[i]) {
                        score++;
                    }
                }
                return(score);
            }

            $(function() {
                $('#gobutton').button().click(function(event) {
                    //do_analysis($('#targettext').val());
                    $('#gobutton').html('<span class="ui-button-text">Running...</span>');
                    setTimeout(function(){
                        plot_many($('#targettext').val(), 200);
                        $('#gobutton').html('<span class="ui-button-text">Go</span>');
                    }, 20);
                });
                $('#mutationspinner').spinner();
                $('#generationspinner').spinner();
                $('#targettext').val(targettext);
                // code for allowing only letters and space (slightly) adapted from
                // http://stackoverflow.com/questions/2980038/allow-text-box-only-for-letters-using-jquery
                $("#targettext").on("keydown", function(event){
                    // Ignore controls such as backspace
                    var arr = [8,16,17,20,35,36,37,38,39,40,45,46];

                    // allow space
                    arr.push(32);

                    // Allow letters
                    for(var i = 65; i <= 90; i++){
                        arr.push(i);
                    }

                    if(jQuery.inArray(event.which, arr) === -1){
                        event.preventDefault();
                    }
                });

                $('#targettext').on("input", function(){
                    var regexp = /[^a-zA-Z ]/g;
                    if($(this).val().match(regexp)){
                        $(this).val( $(this).val().replace(regexp,'') );
                    }
                });
            });
