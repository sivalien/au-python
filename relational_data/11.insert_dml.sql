insert into programs values (1, 'математика и информационные технологии');
insert into programs values (2, 'теоретическая физика');

insert into students(program_id, card, surname, name) values(1, '180101', 'Битов', 'Антон');
insert into students(program_id, card, surname, name) values(2, '180201', 'Аргонова', 'Виолетта');

insert into courses values(1, 'алгебра');
insert into courses values(2, 'физика');
insert into courses values(3, 'математический анализ');
insert into courses values(4, 'алгоритмы');
insert into courses values(5, 'теоритическая механика');
insert into courses values(6, 'программирование на Python');
insert into courses values(7, 'химия');

insert into programs_courses values (1, 1, 1);
insert into programs_courses values (1, 1, 2);
insert into programs_courses values (1, 2, 2);
insert into programs_courses values (1, 3, 1);
insert into programs_courses values (1, 3, 2);
insert into programs_courses values (1, 4, 1);
insert into programs_courses values (1, 5, 2);
insert into programs_courses values (1, 6, 1);
insert into programs_courses values (1, 7, 2);

insert into marks values (1, 1, 4);
insert into marks values (1, 3, 3);
insert into marks values (1, 4, 5);
insert into marks values (1, 6, 5);
insert into marks values (2, 1, 4);
insert into marks values (2, 2, 5);
insert into marks values (2, 3, 4);
insert into marks values (2, 5, 3);
insert into marks values (2, 7, 5);